/*
 * SPDX-License-Identifier: GPL-2.0
 *
 * Copyright (C) 2022 Eric Curtin <ecurtin@redhat.com>
 */

#ifndef _GNU_SOURCE
#define _GNU_SOURCE 1
#endif

#include <errno.h>
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#ifndef PREFIX
#define PREFIX "/usr"
#endif

#define PERR(...)                          \
  do {                                     \
    char* str;                             \
    if (asprintf(&str, __VA_ARGS__) < 0) { \
      perror("");                          \
    } else {                               \
      perror(str);                         \
      free(str);                           \
    }                                      \
  } while (0)

static void print_help() {
  printf("%s\n%s\n", "Usage:", "  ostree-compliance-mode enable");
}

int main(const int argc, const char* argv[]) {
  struct sigaction act;
  act.sa_handler = SIG_IGN;
  for (int i = 1; i < 65; ++i) {
    if (i != SIGKILL && i != SIGSTOP && i != SIGCHLD && i != 32 && i != 33) {
      if (sigaction(i, &act, NULL) < 0) {
        PERR("sigaction(%d, %p, NULL)", i, (void*)&act);
        return errno;
      }
    }
  }

  if (argc < 2 || strncmp(argv[1], "enable", sizeof("enable"))) {
    print_help();
    return 0;
  }

  const uid_t euid = geteuid();
  if (setuid(euid) < 0) {
    PERR("setuid(%d)", euid);
    return errno;
  }

  static const char* file = PREFIX "/libexec/ostree-compliance-mode-helper";
  if (execl(file, file, "enable", (char*)NULL) < 0) {
    PERR("execl(\"%s\", \"%s\", \"enable\", (char*)NULL)", file, file);
    return errno;
  }

  return 0;
}
