import requests

# Test creating a note with background_paper
r1 = requests.post('http://[::1]:8765/api/notes', json={
    "title": "Test Paper Note", 
    "content": "Testing background paper field",
    "background_paper": "grid"
})
print("Create response:", r1.status_code, r1.json())

if r1.status_code == 200:
    note_id = r1.json()['id']
    # Verify in response
    if r1.json().get('background_paper') == 'grid':
        print("SUCCESS: background_paper saved in create")
    else:
        print("FAILURE: background_paper NOT saved in create")
        
    # Test updating background_paper
    r2 = requests.patch(f'http://[::1]:8765/api/notes/{note_id}', json={
        "background_paper": "lined"
    })
    print("Update response:", r2.status_code, r2.json())
    if r2.json().get('background_paper') == 'lined':
        print("SUCCESS: background_paper updated")
    else:
        print("FAILURE: background_paper NOT updated")
    
    # Clean up
    r3 = requests.delete(f'http://[::1]:8765/api/notes/{note_id}')
    print("Delete response:", r3.status_code)
