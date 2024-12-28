import os
import subprocess

def create_config_file():
    # Pfad zur SD-Karte der OUYA (ändere diesen Pfad, falls notwendig)
    path = "/media/OUYA/sdcard/"
    config_content = """OUYA_SERVER_URL=http://ouya.cweiske.de
OUYA_STATUS_SERVER_URL=http://ouya.cweiske.de/api/v1/status
"""
    config_file_path = os.path.join(path, "ouya_config.properties")
    
    with open(config_file_path, 'w') as file:
        file.write(config_content)
    print("Konfigurationsdatei wurde erstellt: " + config_file_path)

def set_dns_server():
    # DNS-Server für das OUYA Setup
    dns_server = "178.254.13.17"
    try:
        subprocess.run(["nmcli", "device", "modify", "eth0", "ipv4.dns", dns_server], check=True)
        print("DNS-Server wurde erfolgreich auf {} gesetzt.".format(dns_server))
    except subprocess.CalledProcessError:
        print("Fehler beim Setzen des DNS-Servers. Bitte manuell setzen oder die Berechtigungen prüfen.")

def reset_dns_server():
    # DNS-Server zurücksetzen (ersetze 'eth0' mit deinem Netzwerkgerät, falls notwendig)
    try:
        subprocess.run(["nmcli", "device", "modify", "eth0", "ipv4.dns", "auto"], check=True)
        print("DNS-Server wurde auf automatisch zurückgesetzt.")
    except subprocess.CalledProcessError:
        print("Fehler beim Zurücksetzen des DNS-Servers. Bitte manuell zurücksetzen oder die Berechtigungen prüfen.")

def main():
    print("OUYA Setup-Skript")
    print("1. Konfigurationsdatei erstellen")
    print("2. DNS-Server setzen")
    print("3. DNS-Server zurücksetzen")
    choice = input("Bitte wählen Sie eine Option: ")
    
    if choice == '1':
        create_config_file()
    elif choice == '2':
        set_dns_server()
    elif choice == '3':
        reset_dns_server()
    else:
        print("Ungültige Auswahl, bitte versuchen Sie es erneut.")

if __name__ == "__main__":
    main()
