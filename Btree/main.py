# This is a sample Python script.
from btree import  Tree
from node import  Node
from data_key_handler import  DataHandler

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
tree_Data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
tree_Data_2 = [23,4,1,23,78,0,34,75,34,13,87,34,98,111,222,333,44,55,66,77,88,999,0]
data_len = len(tree_Data)
tree_degree = 3


tree = Tree(tree_degree)



def add_data_to_tree():
    print("\n================ INSERT TEST ================\n")

    for i in tree_Data_2:
        print(f"\n=== Inserting: {i} ===")
        tree.insert_(DataHandler(i, f"data{i}"))

        result = tree.in_order_traversal(tree.root)
        print(f"Keys in tree:: {[item.ID for item in result]}")
        tree.print_tree()

def delete_test():
    print("\n================ DELETE TEST ================\n")

    keys_to_delete = tree_Data_2

    for i in keys_to_delete:
        print(f"\n=== Deleting: {i} ===")
        tree.delete_key(DataHandler(i))

        if tree.root:
            result = tree.in_order_traversal(tree.root)
            print(f"Keys in tree:: {[item.ID for item in result]}")

            print(f" Tree root - {[k.ID for k in tree.root.keys]}")


            tree.print_tree()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    add_data_to_tree()
    result = tree.in_order_traversal(tree.root)
    print(result)
    delete_test()
    #print(data_len)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
