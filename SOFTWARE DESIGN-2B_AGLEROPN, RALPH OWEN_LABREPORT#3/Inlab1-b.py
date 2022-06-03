#polynomials using linked list
class Node:
    def __init__(self, data, power):
        self.data = data
        self.power = power
        self.next = None

    #  Update node value
    def updateRecord(self, data, power):
        self.data = data
        self.power = power


class AddPolynomial:
    def __init__(self):
        self.head = None

    #  Display given polynomial nodes
    def display(self):
        if (self.head == None):
            print("Empty Polynomial ")

        print(" ", end="")
        temp = self.head
        while (temp != None):
            if (temp != self.head):
                print("+", temp.data, end="")
            else:
                print(temp.data, end="")

            if (temp.power != 0):
                print("x^", temp.power, end=" ", sep="")

            #  Visit to next node
            temp = temp.next

        print(end="\n")

    #  Add node with given data and power
    def addNode(self, data, power):
        if (self.head == None):
            #  Add first node
            self.head = Node(data, power)
        else:
            node = None
            temp = self.head
            location = None
            #  Find the valid new node location
            while (temp != None and temp.power >= power):
                location = temp
                temp = temp.next

            if (location != None and location.power == power):
                #  When polynomial power already exists
                #  Then add current add to previous data
                location.data = location.data + data
            else:
                node = Node(data, power)
                if (location == None):
                    #  When add node in begining
                    node.next = self.head
                    self.head = node
                else:
                    #  When adding node in intermediate
                    #  location or end location
                    node.next = location.next
                    location.next = node

    #  Add two polynomial
    def addTwoPolynomials(self, other):
        #  Define some useful variable
        result = None
        tail = None
        node = None
        #  Get first node of polynomial
        first = self.head
        second = other.head
        #  Execute loop until when polynomial are exist
        #  And add two polynomial.
        #  Process takes O(n) time.
        while (first != None or second != None):
            #  Create node with default value
            node = Node(0, 0)
            if (result == None):
                #  When first resultant node
                result = node

            if (first != None and second != None):
                if (first.power == second.power):
                    #  When the polynomial node power are same
                    node.updateRecord(first.data + second.data, first.power)
                    first = first.next
                    second = second.next
                elif (first.power > second.power):
                    #  When first polynomial power are larger
                    node.updateRecord(first.data, first.power)
                    first = first.next
                else:
                    #  When second polynomial power are larger
                    node.updateRecord(second.data, second.power)
                    second = second.next

            elif (first != None):
                #  When first polynomial are not empty
                #  Update the current node information
                node.updateRecord(first.data, first.power)
                first = first.next
            else:
                #  When second polynomial are not empty
                node.updateRecord(second.data, second.power)
                second = second.next

            if (tail == None):
                tail = node
            else:
                #  Add new node at end of resultant polynomial
                tail.next = node
                tail = node

        #  return first node
        return result


def main():
    poly1 = AddPolynomial()
    poly2 = AddPolynomial()
    result = AddPolynomial()
    #  Add node in polynomial poly1
    poly1.addNode(2, 4)
    poly1.addNode(2, 3)
    poly1.addNode(4, 1)
    poly1.addNode(5, 4)
    poly1.addNode(7, 9)
    #  Add node in polynomial poly2
    poly2.addNode(2, 3)
    poly2.addNode(2, 0)
    poly2.addNode(5, 4)
    poly2.addNode(3, 7)
    #  Display Polynomial nodes
    print("\n Polynomial A")
    poly1.display()
    print(" Polynomial B")
    poly2.display()
    result.head = poly1.addTwoPolynomials(poly2)
    #  Display calculated result
    print(" Result")
    result.display()


if __name__ == "__main__": main()