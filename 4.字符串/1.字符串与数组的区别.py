'''
字符串与数组的区别
'''

'''
字符串是由若干个字符组成的有限序列，可以理解为也给字符数组
在C++中有两种字符串的表达方式
    在char中，是将每一个字符存入了一个数组，并且把结束符\0存入了数组，来表示字符串是否结束的标志
    char a[5] = "asd"
    for (int i = 0; a[i] != '\0'; i++) {
    }
    
    在string这个类中，string类会提供size接口，可以用来判断string类的字符串是否结束，不再需要\0来判断
    string a = "asd"
    for (int i = 0; i < a.size(); i++) {
    }
'''