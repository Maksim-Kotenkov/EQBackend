from EQBackend.EQapp.models import Tests

test = Tests()
test.name = "Test"
test.type = "other"
test.number = 0
test.save()

print("Saved.")
