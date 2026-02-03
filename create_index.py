from endee import Endee

client = Endee()

client.create_index(
    name="employee_policies",
    dimension=384,
    space_type="cosine"
)

print("Index created successfully")
