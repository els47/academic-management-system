# Sistema de Gestão Acadêmica | Python

# 📘 Descrição

Sistema acadêmico desenvolvido em Python com o objetivo de gerenciar informações de cursos, disciplinas, professores, alunos e notas.
O sistema também realiza o cálculo automático de médias, emite relatórios e gera certificados de conclusão conforme os critérios definidos.

# 📋 Requisitos
**Cadastro**

* Cursos: código, nome

* Disciplinas: código, nome

* Professores: matrícula, nome, disciplina, curso

* Alunos: matrícula, nome, curso

* Notas: aluno, disciplina, nota

**Regras de Negócio**

O aluno é aprovado se a média de todas as notas for maior ou igual a 7.

Caso a média seja menor que 7 e maior ou igual a 4, o sistema deverá exibir em quais disciplinas o aluno não obteve nota suficiente e oferecer a opção de alterar a nota nessas disciplinas.

Caso a média seja menor que 4, o sistema deverá informar que o aluno foi reprovado no curso.

**Relatórios e Funcionalidades**

Gerar relatório mostrando todos os alunos matriculados, professores, cursos e disciplinas cadastrados.

Emitir relatórios com todos os alunos matriculados em cada curso e disciplina.

Gerar relatório exibindo o nome do aluno, seus cursos, e todas as notas de todas as disciplinas cursadas por curso.

Para concluir um curso, o aluno deve ter sido aprovado em pelo menos dez disciplinas.

Emitir certificado de conclusão de curso, contendo o nome do aluno, o curso e a data de emissão.

# 🛠️ Tecnologias Utilizadas

Python 3.x

Paradigma de Programação Orientada a Objetos (POO)

Manipulação de dados e relatórios em console (ou arquivos .txt / .csv)

# 🚀 Objetivo do Projeto

Este projeto foi desenvolvido como exercício de lógica de programação e organização de sistemas acadêmicos utilizando Python, simulando o funcionamento básico de um sistema de gestão educacional.
