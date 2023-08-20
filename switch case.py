def age_group(your_age_group):
    group = {
        "below 13": "kid",
        "above 13": "teenager",
        "above 19": "adult",
        "above 60": "retired by government"
    }
    return group[your_age_group, "You have lived well"]


your_age_group = input("Enter your age group : ")
print(f"You are a {age_group(your_age_group)}")
