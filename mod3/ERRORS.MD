## Найденные ошибки и их исправления

### 1. Ошибка в методе get_age
#### Метод возвращает отрицательное значение.
Было:   
<pre><code>def get_age(self):
    now = datetime.datetime.now()
    return <span style="color:red">self.yob - now.year</span>

person = Person('Ksenia', 2003, 'Some street & house')
print(person.get_age())

#будет выведено -20</code></pre>

Стало:
<pre><code>def get_age(self):
    now = datetime.datetime.now()
    return <span style="color:green">now.year - self.yob</span>

person = Person('Ksenia', 2003, 'Some street & house')
print(person.get_age())

#будет выведено 20</code></pre>

### 2. Ошибка в методе set_name
#### Метод не меняет имя человека на введенное name.
Было:   
<pre><code>def set_name(self, name):
    self.name = <span style="color:red">self.name </span>

person = Person('Ksenia', 2003, 'Some street & house')
person.set_name('Ksusha')
print(person.name)

#будет выведено Ksenia, т.е. имя не поменяется</code></pre>

Стало:
<pre><code>def set_name(self, name):
    self.name = <span style="color:green">name </span>

person = Person('Ksenia', 2003, 'Some street & house')
person.set_name('Ksusha')
print(person.name)

#будет выведено Ksusha</code></pre>

### 3. Ошибка в методе set_address
#### При присваивании не используется '=='.
Было:   
<pre><code>def set_address(self, address):
    self.address <span style="color:red">==</span> address</code></pre>

Стало:
<pre><code>def set_address(self, address):
    self.address <span style="color:green">=</span> address</code></pre>

### 4. Ошибка в методе is_homeless
#### NameError: name 'address' is not defined + даже если поменять на self.addresss, то вывод все равно не будет соответствовать описанию.
Было:   
<pre><code>def is_homeless(self):
    """
    return True if address is not set, false in other case
    """
    <span style="color:red">return address is None</span></code></pre>

Стало:
<pre><code>def is_homeless(self):
    """
    return True if address is not set, False in other case
    """
    <span style="color:green">return True if self.address == '' else False</span></code></pre>
