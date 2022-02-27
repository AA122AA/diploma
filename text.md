Если ломается git push, надо ввести команду ssh-add ../путь до ключа

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
#### Устанавливаем zsh и ohmyzsh:
```bash
sudo yum install zsh -y
chsh -s /bin/zsh diploma-server
echo $SHELL
sudo yum install wget git -y
wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh

/bin/cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc
source ~/.zshrc
git clone https://github.com/zsh-users/zsh-autosuggestions ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions
```
#### Устанавливаем docker
```bash 
sudo yum install -y yum-utils
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
sudo systemctl start docker
sudo docker run hello-world
```
Все работает идем дальше
#### Устанавливаем docker compose:
```bash 
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

После установки вышеперечисленного пошел процесс настройки elk стака с нуля.
Спустя 100 правок в каждом yml и conf файле, вроде выведена рабочая
конфигурация. 
Заметка: для того чтобы logstash мог писать в elastic надо создать отдельного
пользователя либо через ui kibana или через post запросы.
Настоить чтоб логи в винде писались в более полном виде
- вход по rdp(успех, не успех)
- Вход по winrm
- Вход по WMI
- Логи на создние таска в планировщике задач 
- Изменение реестра
- Папка автозагрузки 

Посмотреть правила в SIEM
