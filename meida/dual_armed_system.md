## Change config file

### `hebi_description`package
```bash
cd ~/hebi_ws/src/hebi_description
```
```bash
git switch ros2/jazzy-mani-feature-dual
```
```bash
colcon build --symlink-install --packages-select hebi_description
```

### `hebi_moveit_configs`
```bash
cd ~/hebi_ws/src/hebi_moveit_configs
```
```bash
git switch ros2-mani-feature-dual
```
```bash
colcon build --symlink-install --packages-select hebi_moveit_configs
```

### `hebi_bringup`
```bash
cd ~/hebi_ws/src/hebi_bringup
```
```bash
git switch jazzy-mani-feature-dual
```
```bash
colcon build --symlink-install --packages-select hebi_bringup
```

controllers_file: A-2085-06G_controllers.yaml
description_file: A-2085-06G.urdf.xacro
config_file_path: config/arms/A-2085-06G.cfg.yaml