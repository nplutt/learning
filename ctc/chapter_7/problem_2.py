class Call(object):
    def __init__(self, caller, rank=1):
        self.handled = False
        self.caller = caller
        self.rank = rank
        self.handler = None

    def set_rank(self, rank):
        self.rank = rank


class Employee(object):
    def __init__(self, rank):
        self.rank = rank
        self.call = None

    def receive_call(self, call):
        self.call = call

    def finish_call(self):
        self.call = None

    def escalate_and_reassign(self):
        pass

    def is_free(self):
        return self.call is None


class CallCenter(object):
    def __init__(self):
        self.employees = dict(
            respondent=[],
            manager=[],
            director=[]
        )
        self.calls = []

    def add_call(self, call):
        self.calls.append(call)

    def employee_clock_in(self, employee):
        self.employees[employee.rank].append(employee)

    def employee_clock_out(self, employee):
        self.employees[employee.rank].pop()

    def dispatch(self, call):
        for k in self.employees:
            if call.rank <= k:
                for e in k:
                    if e.is_free():
                        call = self.calls.pop(0)
                        e.recieve_call(call)
                        break
        else:
            print("Failed to handle call {}".format(self.calls[0]))
