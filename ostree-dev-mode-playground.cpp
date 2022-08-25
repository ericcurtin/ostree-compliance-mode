#include <ostree-1/ostree-sysroot.h>

int main() {
  GFile *sysroot_file = g_file_new_for_path("/");
  OstreeSysroot *sysroot = ostree_sysroot_new(sysroot_file);
  OstreeDeployment *booted_deployment = ostree_sysroot_get_booted_deployment(sysroot);
}

