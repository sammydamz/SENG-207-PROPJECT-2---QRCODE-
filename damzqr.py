                                                        #PROGRAMMING FOR ENGINEERS - SENG 207
                                                        # SAMUEL DANQUAH ANKAPONG 
                                                        #           10982880
                                                        #          PROJECT 2 - PART 2




import PySimpleGUI as sg
import qrcode



sg.theme('LightPurple')
font = ('Monaco',10)

layout = [
    [sg.Text('Enter a link to generate a QR code:',font = font)],
    [sg.Input(key='link')],
    [sg.Text('Choose a color:',font = font), sg.Combo(values=['green','red','blue','yellow','orange','purple'], default_value='black', key='color', )],
    [sg.Slider(range=(1, 20), orientation='h', default_value=10, key='size')],
    [sg.Button('Generate'), sg.Button('Save As')],
    [sg.Image(key='image')]
]

window = sg.Window('Damz QR Code Generator', layout, font = font)

while True:
    event, values = window.read()
    
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

    if event == 'Generate':
        link = values['link']
        color = values['color']
        size = values['size']
        if link.strip() == "":
            sg.popup_error('Empty Input not acceptable!',font = font)
            continue

        try:
            qr = qrcode.QRCode(version=1,box_size=size, border=3, error_correction=qrcode.constants.ERROR_CORRECT_L)
            qr.add_data(link)
            qr.make(fit=True)
            img = qr.make_image(fill_color=color, back_color='white')
            img.save('qrcode.png')
        except:
            sg.popup_error('Incomplete Input Spcecification Or Invalid input, Try Again!',font = font)
            continue
        
        window['image'].update('qrcode.png')
    
    # Saving the Qr code
    if event == 'Save As':
        filename = sg.popup_get_file('Save Qr Code', save_as=True, default_extension='.png')
        if filename:
            img.save(filename)
    
        

window.close()