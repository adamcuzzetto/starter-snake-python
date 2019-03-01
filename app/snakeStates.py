from statemachine import StateMachine, State
class SnakeStates(StateMachine):
    survive = State('Survive', initial = true)
    findFood = State('Find Food')
    #def SnakeStates(layout):
        