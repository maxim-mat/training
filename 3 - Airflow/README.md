
# Airflow Training Repository

Welcome to the Airflow part of your training! This part contains a collection of resources and exercises designed to help you learn and master Apache Airflow, a powerful orchestration tool that uses DAGs to author, schedule, and manage complex workflows, like as our importers and ETLs
## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Training Materials](#training-materials)
- [Setup](#setup)
- [Exercises](#exercises)

## Introduction

The goals of this part are:

- Understand Airflow’s core concepts and features.
- Learn how to define workflows as Directed Acyclic Graphs (DAGs), and write them efficiently.
- Implement and use various Airflow operators, task groups and decorators.
- Troubleshoot common issues and optimize workflows.
- Write your very first ETL!


## Prerequisites

Before starting the training, ensure you have the following:

- **Python 3.7+**: Airflow requires Python 3.7 or later. You can use your favorite IDE or edit the DAG file directly.
- **Basic Python knowledge**: Familiarity with Python programming is essential for writing Airflow DAGS. Make sure to complete the previous part first.
- **OpenShift**: We'll use the one in Mamdas for certain operators and exercises
  And of course,
-  **Apache Airflow**: We'll use the Airflow installed in Mamdas network, used for training and development.

## Training Materials

https://airflow.apache.org/docs/apache-airflow/stable/tutorial/index.html

	Fundamental Concepts
	Working with TaskFlow
	Building a Running Pipeline

https://airflow.apache.org/docs/apache-airflow/stable/howto/index.html

https://airflow.apache.org/docs/apache-airflow/stable/ui.html

https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/index.html

https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/index.html

https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html

## Setup

Put your python file where your DAG is stored in following path: \\na-dev-nas-1\unix_inst\Software\Shkifut\DataEngineer\kubernetes_nas\AirflowDAGs
Make sure to also save your solutions in a seperate folder, and delete your dags once a senior checked and approved them to clean the folder.
After editing a DAG, wait for a couple of minutes until the code is compiled in Airflow before triggering the DAG.

## exercises
So... what are you waiting for? open your favorite bkm and start the first exercise!
