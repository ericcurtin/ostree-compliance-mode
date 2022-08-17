#include <assert.h>
#include <errno.h>
#include <signal.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

static void print_help() {
  printf("Usage:\n");
}

int main(const int argc, const char* argv[]) {
  struct sigaction act;
  act.sa_handler = SIG_IGN;
  for (int i = 1; i < 65; ++i) {
    if (i != SIGKILL && i != SIGSTOP && i != 32 && i != 33) {
      assert(sigaction(i, &act, NULL) == 0);
    }
  }

  if (argc < 2) {
    print_help();
    return 0;
  }

  if (strncmp(argv[1], "enable", sizeof("enable"))) {
    print_help();
    return 0;
  }

  static const char* file = "/usr/libexec/ostree-dev-mode-helper";
  if (execl(file, file, "enable", (char*)NULL) < 0) {
    return errno;
  }

  return 0;
}
