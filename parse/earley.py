import re
import copy

class State(object):
    """docstring for State"""
    num = 0
    def __init__(self, rule, dotPos, orig_pos, end_pos, back_pointers=[]):
        self.index = State.num
        State.num += 1
        self.rule = rule
        self.dotPos = dotPos
        self.orig_pos = orig_pos
        self.end_pos = end_pos
        self.back_pointers = list(back_pointers)
    def __repr__(self):
        terms = [str(p) for p in self.rule.production]
        terms.insert(self.dotPos, u"$")
        pointers = " ".join(str(i.index) for i in self.back_pointers)
        return "%d. %-1s -> %-8s [%s-%s] [%-s]" % (self.index, self.rule.variable, " ".join(terms), self.orig_pos, self.end_pos, pointers)
    def __eq__(self, other):
        if not isinstance(other, State):
            return False
        return (self.rule, self.dotPos, self.orig_pos, self.back_pointers) == (other.rule, other.dotPos, other.orig_pos, other.back_pointers)
    def __ne__(self, other):
        return not (self == other)
    def __hash__(self):
        return hash((self.rule, self.dotPos, self.orig_pos))
    def finished(self):
        return self.dotPos >= len(self.rule.production)
    def next(self):
        if self.finished():
            return None
        return self.rule.production[self.dotPos]

class Tree(object):
    def __init__(self, data=None, children=None):
        self.children = []
        if children is not None:
            self.children.extend(children)
        self.data = data
    def add(self, child):
        self.children.append(child)
    def print(self, level=0):
        text = "\t"*level+str(self.data)
        print(text)
        for child in self.children:
            child.print(level+1)

class Parser(object):
    """docstring for Parser"""
    def __init__(self, grammar):
        self.grammar = grammar

    def __init_states(self, text):
        self.state_list = []
        self.text = text
        for k in range(len(self.tokens)+1):
            self.state_list.append(set())

    def tokenize(self, text):
        self.tokens = re.split(self.grammar.delim, text)

    def parse(self, text):
        self.tokenize(text)
        self.__init_states(text)
        self.state_list[0].add(State(self.grammar.topRule, 0, 0, 0))
        for k in range(len(self.tokens)+1):
            #print("\nk = %d" % k)
            active = set(self.state_list[k])
            seen = set(self.state_list[k])
            while active:
                for state in active:
                    if not state.finished():
                        if not self.grammar.is_terminal(state.next()):
                            self.predict(state, k)
                        else:
                            self.scan(state, k)
                    else:
                        self.complete(state, k)
                seen |= active
                active = self.state_list[k]-seen
            # print()
            # for state in self.state_list[k]:
            #     print(state)
        result = []
        for st in self.state_list[-1]:
            if st.rule == self.grammar.topRule:
                result.append(self.construct_tree(st))
        return result

    def predict(self, state, k):
        for rule in self.grammar:
            if state.next() == rule.variable:
                self.state_list[k].add(State(rule, 0, k, k))

    def scan(self, state, k):
        if k >= len(self.tokens):
            return
        if state.next().part_of(self.tokens[k]):
            self.state_list[k+1].add(State(copy.deepcopy(state.rule), state.dotPos+1, state.orig_pos, k+1, state.back_pointers))

    def complete(self, state, k):
        for s in self.state_list[state.orig_pos]:
            if s.next() == state.rule.variable:
                newState = State(s.rule, s.dotPos+1, s.orig_pos, k, s.back_pointers)
                newState.back_pointers.append(state)
                self.state_list[k].add(newState)

    def construct_tree(self, state, level=0):
        tree = Tree()
        tree.data = state.rule.variable
        tree.fn_enter = state.rule.fn_enter
        tree.fn_exit = state.rule.fn_exit
        j = 0
        for i in range(len(state.rule.production)):
            node = Tree()
            node.fn_enter = None
            node.fn_exit = None
            if state.back_pointers:
                if not self.grammar.is_terminal(state.rule.production[i]):
                    node = self.construct_tree(state.back_pointers[j], level+1)
                    j += 1
            node.data = state.rule.production[i]
            tree.add(node)
        return tree