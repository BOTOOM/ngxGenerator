
class filters:

    def space_case(self,n):
        x=n.split("_")
        temp = ""
        for t in x :
            temp += t.capitalize()+" "
        return temp[0:-1]

    def upper_camel_case(self,n):
        x=n.split("_")
        temp = ""
        for t in x :
            temp += t.capitalize()
        return temp

    def lower_camel_case(self,n):
        x=n.split("_")
        temp = ""
        temp += x[0].lower()
        for t in x[1:] :
            temp += t.capitalize()
        return temp

    def kebab_case(self,n):
        x=n.split("_")
        temp = ""
        temp += x[0].lower()
        for t in x[1:] :
            temp += "-"+t
        return temp

