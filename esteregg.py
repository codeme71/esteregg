class SimplePerlInterpreter:
    def __init__(self):
        self.variables = {}

    def eval(self, code):
        lines = code.strip().split('n')
        for line in lines:
            self.execute_line(line)

    def execute_line(self, line):
        line = line.strip()
        
        # Присваивание переменной
        if '=' in line:
            var_name, value = map(str.strip, line.split('=', 1))
            self.variables[var_name] = self.evaluate_expression(value)
        
        # Печать переменной или значения
        elif line.startswith('print'):
            expr = line[5:].strip(' ();')
            print(self.evaluate_expression(expr))

    def evaluate_expression(self, expr):
        # Удаляем пробелы
        expr = expr.replace(' ', '')
        
        # Обработка простых чисел и переменных
        if expr.isdigit():
            return int(expr)
        elif expr in self.variables:
            return self.variables[expr]
        
        # Поддержка сложения и умножения

    def evaluate_arithmetic(self, expr):
        # Сначала обрабатываем умножение
        if '*' in expr:
            parts = expr.split('*')
            result = 1
            for part in parts:
                result *= self.evaluate_arithmetic(part)
            return result
        
        # Затем обрабатываем сложение
        if '+' in expr:
            parts = expr.split('+')
            return sum(self.evaluate_arithmetic(part) for part in parts)

        # Если не осталось операторов, возвращаем значение
        return int(expr) if expr.isdigit() else self.variables.get(expr)
        
  # Пример использования
esteregg = SimplePerlInterpreter()

# Код на "перле"
perl_code = ""
$var1 = 15;
$var2 = 12;
$var3 = $var1 + $var2;
$var4 = $var1 * $var2;
print $var3; 
print $var4; 
""

esteregg.eval(perl_code)

// esteregg              

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
        

