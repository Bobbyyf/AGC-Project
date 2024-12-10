import os
import time
import BurnBabyBurn
import calculator
import Graph
import HashCodes

def countdown():
    for i in range(5, 0, -1):
        print(f"T-{i}")
        time.sleep(1)
    print("EXECUTE")

def main():
    launch_tree = BurnBabyBurn.LaunchTree()
    
    print("=== Launch Control System Initialized ===")
    print("Enter access codes to execute launch sequence stages.")
    print("Enter 'status' to check current status.")
    print("Enter 'abort' to exit.")

    graph = Graph.BipartiteGraph()
    graph.makeGraph()
    
    while not launch_tree.is_sequence_complete():
        launch_tree.display_sequence()
        current_stage = launch_tree.get_current_stage_info()
        
        if not current_stage:
            print("\nAll stages complete!")
            break
            
        command = input("\nEnter access code or command: ").strip().upper()
        
        if command == 'ABORT':
            print("Launch sequence aborted by operator")
            break
        elif command == 'STATUS':
            print("\nPending stages:", launch_tree.get_pending_stages())
            print(f"Current stage: {current_stage}")
        else:
            if graph.getCodeExists(command) == True:
                success = launch_tree.execute_stage_with_code(command)
            else:
                print("INVALID COMMAND")
                break
            
            if success:
                print("Stage completed successfully!")
            else:
                print("Stage execution failed. Please try again.")

    if(launch_tree.is_sequence_complete()):
        print("\n=== Launch Sequence Successfully Completed! ===")
        countdown()
    else:
        print("\n=== Launch Sequence Incomplete - Check Systems ===")

if __name__ == "__main__":
    main()