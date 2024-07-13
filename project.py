class Node:
    def __init__(self):
        self.data = ['\0'] * 4 
        self.next = None  

class DynamicString:
    def __init__(self, initial_str=""):
        self.head = None  
        self.length = 0  
        if initial_str:
            self.append(initial_str)

    def append(self, string):
        str_len = len(string)  
        self.length += str_len 

        if self.head is None:
            self.head = Node()
        
        current = self.head 
        
        while current.next is not None:
            current = current.next
        while str_len > 0:
            if '\0' in current.data:
                fill_index = current.data.index('\0')  
                fill_count = min(4 - fill_index, str_len) 
                current.data[fill_index:fill_index + fill_count] = list(string[:fill_count])
                string = string[fill_count:]
                str_len -= fill_count
            if str_len > 0:
                new_node = Node()
                current.next = new_node
                current = new_node

    def print_string(self):
        current = self.head  
        result = ''
        while current is not None:
            result += ''.join(current.data).replace('\0', '')  
            current = current.next  
        print(result) 

    def clear(self):
        self.head = None  
        self.length = 0  

    def get_length(self):
        return self.length  


str_obj = DynamicString("String1")
str_obj.append("String2")
str_obj.append("String3")
str_obj.append("String4")
str_obj.append("String5")
str_obj.print_string() 


print("Length of string:", str_obj.get_length())  
str_obj.clear()
print("Length after clear:", str_obj.get_length()) 
str_obj.print_string()  
