#!/bin/bash

# Add kubectl alias
echo "alias k=kubectl" >> ~/.bashrc
echo "complete -F __start_kubectl k" >> ~/.bashrc

# Enable kubectl autocompletion
echo "source <(kubectl completion bash)" >> ~/.bashrc

# Reload bashrc if in interactive mode
if [[ $- == *i* ]]; then
    source ~/.bashrc
    echo "Shell updated with kubectl alias and completion!"
else
    echo "Alias and completions added. Please run 'source ~/.bashrc' or restart terminal."
fi
