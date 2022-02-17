# scripts

### pacman command for installing non-AUR packages: 
```
pacman -S --needed $(comm -12 <(pacman -Slq | sort) <(sort packages.txt))
```
