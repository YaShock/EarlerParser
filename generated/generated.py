from . import semantics
dict = {}
def create():
    dict[2804851109224] = (semantics.expr_enter, semantics.expr_exit)
    dict[2804851109504] = (semantics.sum_enter, semantics.sum_exit)
    dict[2804851109560] = (semantics.sum_unary_enter, semantics.sum_unary_exit)
    dict[2804851109840] = (semantics.product_enter, semantics.product_exit)
    dict[2804851187840] = (semantics.product_unary_enter, semantics.product_unary_exit)
    dict[2804851188568] = (semantics.terminal_enter, semantics.terminal_exit)
    dict[2804851188736] = (semantics.terminal_enter, semantics.terminal_exit)
    dict[2804851188960] = (semantics.terminal_enter, semantics.terminal_exit)
    dict[2804851189184] = (semantics.terminal_enter, semantics.terminal_exit)
    dict[2804851189408] = (semantics.terminal_enter, semantics.terminal_exit)
    dict[2804851189632] = (semantics.terminal_enter, semantics.terminal_exit)
    dict[2804851189856] = (semantics.terminal_enter, semantics.terminal_exit)
    dict[2804851190080] = (semantics.terminal_enter, semantics.terminal_exit)
    dict[2804851190304] = (semantics.terminal_enter, semantics.terminal_exit)
    dict[2804851190528] = (semantics.terminal_enter, semantics.terminal_exit)
    dict[2804851188120] = (semantics.operator_expr_enter, semantics.operator_expr_exit)
    dict[2804851190696] = (semantics.operator_expr_enter, semantics.operator_expr_exit)
    dict[2804851190976] = (semantics.operator_term_enter, semantics.operator_term_exit)
    dict[2804851191256] = (semantics.operator_term_enter, semantics.operator_term_exit)