# JUPYTER NOTEBOOK STARTUP SCRIPT 

# Enable jupyter extensions
jupyter contrib nbextension install --sys-prefix > /dev/null 2>&1
jupyter nbextension enable scratchpad/main --sys-prefix > /dev/null 2>&1
# jupyter nbextension enable toc2/main --sys-prefix > /dev/null 2>&1
jupyter nbextension enable execute_time/ExecuteTime --sys-prefix > /dev/null 2>&1
jupyter nbextension enable hide_input_all/main --sys-prefix > /dev/null 2>&1
jupyter nbextension enable collapsible_headings/main --sys-prefix > /dev/null 2>&1
jupyter nbextension enable spellchecker/main --sys-prefix > /dev/null 2>&1

# Kickstart jupyter notebook
jupyter notebook --ip 0.0.0.0 --port 8080 --allow-root &