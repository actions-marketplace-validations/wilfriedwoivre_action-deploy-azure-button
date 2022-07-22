# Github Action : Deploy Azure Button

Github Action to automate generation of Deploy to Azure button.

Usage :

```yaml
    - name: generate-deploy-button
      id: generate-deploy-button
      uses: wilfriedwoivre/action-deploy-azure-button@v1
      env:
        templatePath: ${{ matrix.template }}
        markdownPath: ${{ matrix.markdown }}
```

Only update local files, you must push your code after update.

## Parameters

| Parameter Name | Mandatory | Default Value |
| -- | -- | -- |
| templatePath | false | azuredeploy.json
| markdownPath | false | README.md
| branchName | false | master
| targetAzureUrl | false | https://portal.azure.com/#create/Microsoft.Template/uri/

To deploy Azure policy override the targetAzureUrl with this value : https://portal.azure.com/#blade/Microsoft_Azure_Policy/CreatePolicyDefinitionBlade/uri/

## Output

| Output Name |
| -- |
| fileUpdated

## Samples

Simple workflow, to update only one Readme :

```yaml
name: Deploy Azure Button

on:
  push

jobs:
  add-azure-deploy-button:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2

    - name: generate-deploy-button
      id: generate-deploy-button
      uses: wilfriedwoivre/action-deploy-azure-button@v1

    - name: push-update
      if: steps.generate-deploy-button.outputs.fileUpdated == 'True'
      run: |
          git config --global user.name 'Gitub Action Bot'
          git config --global user.email 'wilfried.woivre@users.noreply.github.com'
          git diff --quiet && git diff --staged --quiet || git commit -am "Add Azure deploy button"
          git push
```

Powerfull of this action is when you use strategy matrix to update templatePath and markdownPath like that

```yaml
  add-azure-deploy-button:
    needs:
      - generate-matrix
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      max-parallel: 2
      matrix: ${{ fromJson(needs.generate-matrix.outputs.matrix)  }}

    steps:
    - uses: actions/checkout@v2

    - name: generate-deploy-button
      id: generate-deploy-button
      uses: wilfriedwoivre/action-deploy-azure-button@master
      env:
        templatePath: ${{ matrix.template }}
        markdownPath: ${{ matrix.markdown }}

    - name: push-update
      if: steps.generate-deploy-button.outputs.fileUpdated == 'True'
      run: |
        git config --global user.name 'Gitub Action Bot'
        git config --global user.email 'wilfried.woivre@users.noreply.github.com'
        git diff --quiet && git diff --staged --quiet || git commit -am "Add Azure deploy button"
        git pull --rebase
        git push
```
