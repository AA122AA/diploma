1. Скачал минимальный образ с оф сайта 
## Конфиг для diploma-server
1. Конфиг ВМ: 2core-1GB-40GB
1. Стандартная установка с авторазметкой диска
1. Все пароли - 0000
### Комманды для настройки: 
```bash
sudo yum update
```
#### Устанавливаю virtualbox guest additions:
```bash
yum install dkms gcc make kernel-devel bzip2 binutils patch libgomp glibc-headers glibc-devel kernel-headers elfutils-libelf-devel
mkdir -p /media/cdrom
mount /dev/scd0 /media/cdrom
sh /media/cdrom/VBoxLinuxAdditions.run
sudo reboot
```
#### Настраиваем ssh, чтоб было удобно работать:
```bash
sudo yum -y install net-tools vim

```
#### Устанавливаем docker
```bash 
sudo yum install -y yum-utils
