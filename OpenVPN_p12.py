#!/usr/bin/env python3
import tkinter as tk
import subprocess
import os

def connect():
    login = login_entry.get()
    password = password_entry.get()
    pin = pin_entry.get()

    # Run OpenVPN connection command with login, password, and pin
    subprocess.Popen(['sudo', 'openvpn', '--config', config_path.get(), '--auth-user-pass', 'credentials.txt', '--pkcs12', cert_path.get(), '--askpass', 'passphrase.txt'])

    # Create a temporary credentials file
    with open('credentials.txt', 'w') as file:
        file.write(f"{login}\n{password}")

    # Create a temporary passphrase file
    with open('passphrase.txt', 'w') as file:
        file.write(pin)

def disconnect():
    # Run OpenVPN disconnection command
    subprocess.Popen(['killall', 'openvpn'])

def update_status():
    # Check if OpenVPN is running
    result = subprocess.run(['pgrep', '-x', 'openvpn'], capture_output=True)
    if result.returncode == 0:
        status_label.config(text="Status: Connected", fg="green")
    else:
        status_label.config(text="Status: Disconnected", fg="red")

def cleanup():
    # Remove the temporary credentials and passphrase files
     
     if os.path.exists('credentials.txt'):
        os.remove('credentials.txt')
     if os.path.exists('passphrase.txt'):  
        os.remove('passphrase.txt')

window = tk.Tk()
window.title("OpenVPN GUI")

config_label = tk.Label(window, text="Config Path:")
config_label.pack()

config_path = tk.Entry(window)
config_path.pack()

cert_label = tk.Label(window, text="Cert Path:")
cert_label.pack()

cert_path = tk.Entry(window)
cert_path.pack()

login_label = tk.Label(window, text="Login:")
login_label.pack()

login_entry = tk.Entry(window)
login_entry.pack()

password_label = tk.Label(window, text="Password:")
password_label.pack()

password_entry = tk.Entry(window, show="*")
password_entry.pack()

pin_label = tk.Label(window, text="Cert PIN:")
pin_label.pack()

pin_entry = tk.Entry(window, show="*")
pin_entry.pack()

connect_button = tk.Button(window, text="Connect", command=connect)
connect_button.pack()

disconnect_button = tk.Button(window, text="Disconnect", command=disconnect)
disconnect_button.pack()

status_label = tk.Label(window, text="Status: Disconnected", fg="red")
status_label.pack()

update_button = tk.Button(window, text="Update Status", command=update_status)
update_button.pack()

window.protocol("WM_DELETE_WINDOW", cleanup)

window.mainloop()
