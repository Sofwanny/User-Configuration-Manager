def add_setting(dict_settings, tuple_dict):
    key, value = tuple_dict 
    key = key.lower() 
    value = value.lower() 
    if key in dict_settings: 
        return f"Setting '{key}' already exists! Cannot add a new setting with this name." 
    else: 
        dict_settings[key] = value 
        return f"Setting '{key}' added with value '{value}' successfully!" 
        
def update_setting(settings, tuple_setting): 
    key, value = tuple_setting 
    key = key.lower() 
    value = value.lower() 
    if key in settings:
        settings[key] = value 
        return f"Setting '{key}' updated to '{value}' successfully!" 
    else: 
         
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings, key): 
    key = key.lower()
    
    if key in settings:
        del settings[key] 
        return f"Setting '{key}' deleted successfully!"  
    else:
        return 'Setting not found!'

def view_settings(settings):
    if not settings:
        return "No settings available."
    else:
        lines = []
        for key, value in settings.items():
            cap_key = str(key).capitalize()
            lines.append(f"{cap_key}: {value}")
        return "Current User Settings:\n" + "\n".join(lines)+ "\n"                         
print(view_settings({'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'})) 


test_settings = {
    'theme': 'dark', 
    'notifications': 'enabled', 
    'volume': 'high'
}       