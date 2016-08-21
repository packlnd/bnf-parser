def generate(goal):
    asm = Asm()
    generate_goal(goal, asm)

def generate_goal(goal, asm):
    generate_main(goal.main, asm)

def generate_main(main, asm):
    for stmt in main.statements:
        generate_stmt(stmt, asm)
