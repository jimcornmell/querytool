# Command line completion file for query.

_query () {
  local cur prev opts
  COMPREPLY=()
  local cur="${COMP_WORDS[COMP_CWORD]}"
  local prev="${COMP_WORDS[COMP_CWORD-1]}"
  # local IFS=$'\n'

  if [[ ${cur} == -* ]] ; then
    local opts="-l --list-databases -h --help -d --database -n --no-header -c --count -s --show-query -t --show-time -v --verbose -j --json -m --simple -f --format -o --output --version"
    COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
    return 0
  else
    if [[ ${COMP_CWORD} -eq 1 ]] ; then
      local sql_files=$(find . -maxdepth 2 -name '*.sql' | cut -c 3- | sort -u)
      COMPREPLY=($(compgen -W "${sql_files}" -- "${cur}"))
      return 0
    fi
  fi

  case "${prev}" in
    -d|--database)
      local databases=$(grep "^\[" ~/.ssh/secret_keys/query.properties | sed -e 's/^\[db.//' -e 's/]$//')
      COMPREPLY=( $(compgen -W "${databases}" -- ${cur}) )
      ;;
    -f|--format)
      local formats="plain simple github grid fancy_grid pipe orgtbl jira presto pretty psql rst mediawiki moinmoin youtrack html latex latex_raw latex_booktabs textile"
      COMPREPLY=( $(compgen -W "${formats}" -- ${cur}) )
      ;;
    -o|--output)
      local outputs="output_file.csv output_file.xlsx output_file.sql output_file.html output_file.json"
      COMPREPLY=( $(compgen -W "${outputs}" -- ${cur}) )
      ;;
    *)
      local sql_files=$(find . -maxdepth 2 -name '*.sql' | cut -c 3- | sort -u)
      COMPREPLY=($(compgen -W "${sql_files}" -- "${cur}"))
      ;;
  esac
}

complete -F _query query

