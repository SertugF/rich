from rich.console import Console


recorder = Console(record=True)

with recorder.capture(echo=False) as capture:
    recorder.print("foo")

# when there is on recorde it works fine
recorded_text = recorder.export_text()

str = capture.get()

if recorded_text == "foo\n":
    print("Test1: Success")
else:
    print("Test1: Failed")

if str == "foo\n":
    print("Test2: Success")
else:
    print("Test2: Failed")

with recorder.capture(echo=False) as capture:
    recorder.print("Hello")
    recorder.print("World")

# when there is more than one record it doesnt work. captures first record twice
recorded_text = recorder.export_text()

str = capture.get()

if recorded_text == "Hello\nWorld\n":
    print("Test1: Success")
else:
    print("Test1: Failed")

if str == "Hello\nWorld\n":
    print("Test2: Success")
else:
    print("Test2: Failed")


with recorder.capture(echo=True) as capture:
    recorder.print("Foo")
    recorder.print("Bar")


if capture.get() == "Foo\nBar\n":
    print("Test2: Success")
else:
    print("Test2: Failed")


recorded_text = recorder.export_text()
# out, err = self.capsys.readouterr()


if recorded_text == "Hello\nWorld\nFoo\nBar\n":
    print("Test3: Success")
else:
    print("Test3: Failed")

# if out == "Foo\nBar\n":
 #   print("Test4: Success")
# else:
 #   print("Test4: Failed")


recorder2 = Console(record=True)
recorder3 = Console(record=True)
recorder4 = Console(record=True)
recorder5 = Console(record=True)

with recorder.capture():
    recorder.print("foo")
str = recorder.export_text()  # correctly captures
print("Test1")  # correctly prints
print(str)  # correctly prints


recorder2.begin_capture()
recorder2.print("foo")
recorder2.end_capture()
str2 = recorder2.export_text()  # correctly captures
print("Test2")  # correctly prints
print(str2)  # correctly prints

print("-------------------------------------------------------")

with recorder3.capture(echo=True):
    recorder3.print("foo")  # should print foo , doesnt work
str3 = recorder3.export_text()  # correctly captures
print("Test3")  # correctly prints
print(str3)  # correctly prints
# output must be foo , Test3 , foo ,

print("-------------------------------------------------------")
with recorder4.capture(echo=False):
    recorder4.print("foo")  # should not print, works correctly
str4 = recorder4.export_text()  # correctly captures
print("Test4")  # correctly prints
print(str4)  # correctly prints

print("-------------------------------------------------------")

with recorder5.capture(echo=True):
    recorder5.print("foo")  # should print foo , doesnt work
    recorder5.print("foo")  # should print foo , doesnt work
    recorder5.print("foo")  # should print foo , doesnt work
str5 = recorder5.export_text()  # correctly captures
print("Test5")  # correctly prints
print(str5)  # correctly prints
# output must be foo , Test3 , foo ,
