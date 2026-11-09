from pyscript import display, document

def get_element(e):
    document.getElementById('result').innerHTML = " "

    gotten_element = document.getElementById('em').value.strip().title()

    elements = {'H':'Hydrogen', 'C':'Carbon', 'N':'Nitrogen','O':'Oxygen','P':'Phosphorus','S':'Sulfur','Se':'Selenium','F':'Fluorine','Cl':'Chlorine','Br':'Bromine','I':'Iodine','At':'Astatine','He':'Helium','Ne':'Neon','Ar':'Argon','Kr':'Krypton','Xe':'Xenon','Rn':'Radon'}
    atomic_nums = {'H':'1', 'C':'6', 'N':'7','O':'8','P':'15','S':'16','Se':'34','F':'9','Cl':'17','Br':'35','I':'53','At':'85','He':'2','Ne':'10','Ar':'18','Kr':'36','Xe':'54','Rn':'86'}
    atomic_heaviness = {'H': '1.008', 'C': '12.011', 'N': '14.007', 'O': '15.999', 'P': '30.974', 'S': '32.07', 'Se': '78.97', 'F': '18.998', 'Cl': '35.45', 'Br': '79.90', 'I': '126.90', 'At': '210', 'He': '4.0026', 'Ne': '20.180', 'Ar': '39.95', 'Kr': '83.80', 'Xe': '131.29', 'Rn': '222'}

    em_check = gotten_element in elements

    outputs = (
        ('Sorry, your element is not in the list!',),
        (f"Element: {elements.get(gotten_element)}",
         f"Symbol: {gotten_element}",
         f"Atomic Number: {atomic_nums.get(gotten_element)}",
         f"Atomic Mass: {atomic_heaviness.get(gotten_element)}")
    )

    display(*outputs[em_check], target='result')