project('ostree-compliance-mode', 'c',
    meson_version : '>= 0.50',
    default_options : [
        'werror=true',
        'warning_level=3',
        'c_std=gnu11'
    ])

add_project_arguments(
  '-Wstrict-aliasing',
  '-Wchar-subscripts',
  '-Wformat-security',
  '-Wmissing-declarations',
  '-Wpointer-arith',
  '-Wshadow',
  '-Wsign-compare',
  '-Wtype-limits',
  '-Wunused-function',
  '-Wno-unused-variable',
  '-Wno-implicit-function-declaration',
  '-DPREFIX="'+get_option('prefix')+'"',
  language: 'c'
)

ostree_compliance_mode_sources = files([
    'ostree-compliance-mode.c'
])

ostree_compliance_mode  = executable('ostree-compliance-mode', ostree_compliance_mode_sources, install : true)

