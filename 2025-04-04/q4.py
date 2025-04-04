# Q4 Develop a Python-based Hoare Logic verifier for simple imperative programs

from dataclasses import dataclass
from typing import Union


# === Expressions and Boolean Conditions ===

@dataclass
class Expr:
    pass


@dataclass
class Var(Expr):
    name: str


@dataclass
class Const(Expr):
    value: int


@dataclass
class BinOp(Expr):
    op: str  # '+', '-', '*'
    left: Expr
    right: Expr


@dataclass
class BoolExpr:
    pass


@dataclass
class RelOp(BoolExpr):
    op: str  # '==', '!=', '<', '<=', '>', '>='
    left: Expr
    right: Expr


# === Commands ===

@dataclass
class Cmd:
    pass


@dataclass
class Skip(Cmd):
    pass


@dataclass
class Assign(Cmd):
    var: str
    expr: Expr


@dataclass
class Seq(Cmd):
    first: Cmd
    second: Cmd


@dataclass
class If(Cmd):
    cond: BoolExpr
    then_cmd: Cmd
    else_cmd: Cmd


@dataclass
class While(Cmd):
    cond: BoolExpr
    body: Cmd
    invariant: 'Assertion'


# === Assertions ===

@dataclass
class Assertion:
    expr: str  # A logical formula as a string (placeholder logic)


# === Helper Functions ===

def expr_to_str(e: Expr) -> str:
    if isinstance(e, Var):
        return e.name
    elif isinstance(e, Const):
        return str(e.value)
    elif isinstance(e, BinOp):
        return f"({expr_to_str(e.left)} {e.op} {expr_to_str(e.right)})"
    else:
        return "?"


def bool_expr_to_str(b: BoolExpr) -> str:
    if isinstance(b, RelOp):
        return f"{expr_to_str(b.left)} {b.op} {expr_to_str(b.right)}"
    else:
        return "?"


# === Verifier Function ===

def verify(assertion_pre: Assertion, cmd: Cmd, assertion_post: Assertion) -> bool:
    if isinstance(cmd, Skip):
        return assertion_pre.expr == assertion_post.expr

    elif isinstance(cmd, Assign):
        # Assignment Rule: {P[x := E]} x := E {P}
        substituted = assertion_post.expr.replace(cmd.var, f"({expr_to_str(cmd.expr)})")
        return assertion_pre.expr == substituted

    elif isinstance(cmd, Seq):
        # Sequential composition: manual intermediate assertion needed
        print("Sequential composition requires a manually provided intermediate assertion.")
        return False

    elif isinstance(cmd, If):
        return (verify(Assertion(f"({assertion_pre.expr}) and ({bool_expr_to_str(cmd.cond)})"),
                       cmd.then_cmd, assertion_post) and
                verify(Assertion(f"({assertion_pre.expr}) and (not ({bool_expr_to_str(cmd.cond)}))"),
                       cmd.else_cmd, assertion_post))

    elif isinstance(cmd, While):
        inv = cmd.invariant
        cond_str = bool_expr_to_str(cmd.cond)
        body_ok = verify(Assertion(f"({inv.expr}) and ({cond_str})"), cmd.body, inv)
        post_ok = inv.expr == f"({assertion_post.expr})"
        return body_ok and post_ok

    else:
        print("Unknown command type.")
        return False


# === Test Example ===

if __name__ == "__main__":
    # Example: x := x + 1
    pre = Assertion("x == 0")
    cmd = Assign("x", BinOp("+", Var("x"), Const(1)))
    post = Assertion("x == 1")

    result = verify(pre, cmd, post)
    print("Hoare triple is valid:", result)
