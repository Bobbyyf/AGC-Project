import main


class LaunchStageNode:
    def __init__(self, code_name, access_code):
        self.code_name = code_name
        self.access_code = access_code
        self.data = "no"
        self.children = []
        self.parent = None

class LaunchTree:
    def __init__(self):
        self.root = None
        self.current_stage = None
        self.initialize_sequence()
    
    def initialize_sequence(self):
        stages = []
        stages.append(("Pre-launch Systems Check", "1901")),
        stages.append(("Fuel Pressurization", "1902")),
        stages.append(("Ignition Sequence Start", "1903")),
        stages.append(("Main Engine Ignition", "1904")),
        stages.append(("Liftoff Clearance", "1905")),
        stages.append(("Abort System Monitoring", "1906"))

        self.root = LaunchStageNode(stages[0][0], stages[0][1])
        self.current_stage = self.root
        
        current = self.root
        for stage_name, access_code in stages[1:]:
            new_node = LaunchStageNode(stage_name, access_code)
            new_node.parent = current
            current.children.append(new_node)
            current = new_node

    def execute_stage_with_code(self, entered_code):
        if not self.current_stage:
            print("No current stage")
            return False
        
        if entered_code != self.current_stage.access_code:
            print("Invalid code")
            return False
        
        
        if self.current_stage.children:
            self.current_stage.data = "yes"
            self.current_stage = self.current_stage.children[0]
        else:
            self.current_stage = "yes"
            self.current_stage = None
            
        print("Executed")
        return True

    def is_sequence_complete(self):
        def check_node(node):
            if node is None:
                return True
            if node.data != "yes":
                return False
            for child in node.children:
                if not check_node(child):
                    return False
            return True
        
        return check_node(self.root)

    def display_sequence(self):
        def display_node(node, level=0):
            if node:
                print(node.code_name)
                for child in node.children:
                    display_node(child, level + 1)
                    
        print("\nSequence:")
        display_node(self.root)

    def get_current_stage_info(self):
        if self.current_stage:
            return self.current_stage.code_name
        return None

    def get_pending_stages(self):
        pending = []
        
        def collect_pending(node):
            if node and node.data == "no":
                pending.append(node.code_name)
            for child in node.children:
                collect_pending(child)
                
        collect_pending(self.root)
        return pending


