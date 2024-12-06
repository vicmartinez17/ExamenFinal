cmake_minimum_required(VERSION 3.8)
project(robot_description)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Encuentra dependencias necesarias
find_package(ament_cmake REQUIRED)

# Configuración para la instalación de archivos de configuración y lanzamiento
install(
  DIRECTORY urdf
  DESTINATION share/${PROJECT_NAME}
)

install (
  DIRECTORY launch/
  DESTINATION share/${PROJECT_NAME}/launch
)

install (
  DIRECTORY config/
  DESTINATION share/${PROJECT_NAME}/config
)

# Configuración para pruebas (opcional)
if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # Las siguientes líneas omiten algunos verificadores para facilitar la compilación inicial
  set(ament_cmake_copyright_FOUND TRUE)
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

# Finaliza la configuración del paquete
ament_package()
