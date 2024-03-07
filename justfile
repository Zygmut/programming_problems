set shell := ['nu', '-m', 'light', '-c']

proj_dir := justfile_directory()

_:
    @just -l

create name lang:
    @mkdir "{{ proj_dir }}/{{ name }}"
    @cp "{{ proj_dir }}/.templates/main.{{ lang }}" "{{ proj_dir }}/{{ name }}"
    @echo "Created \"{{ name }}\""
