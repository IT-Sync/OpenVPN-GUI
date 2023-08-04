# OpenVPN-GUI
Для работы необходимо установить python-tk
Astra-Linux
  sudo apt install python3-tk

Сделать файл исполняемым:
  chmod a+x OpenVPN_p12.py

#Запуск от имени обычного пользователя
Для запуска от имени обычного пользователя, необходимо:
  vi \etc\sudoers
Добавить:
  user ALL=(all) NOPASSWD: /usr/sbin/openvpn
