{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMm3rlw2QDXTTsm+5NfKDcB",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/26b21a4278kiet-ui/SPORTS-TEAM-RATING-SYSTEM-/blob/main/Sample.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "EMD2yqW5hNSW",
        "outputId": "eb5e9ff9-0465-4812-af3a-cd5f767a2820",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "=======================================================\n",
            "Sports Team Rating System\n",
            "=======================================================\n",
            "Benchmark Dataset : Custom College Football Benchmark\n",
            "Number of Teams   : 5\n",
            "Number of Matches : 10\n",
            "=======================================================\n"
          ]
        }
      ],
      "source": [
        "# ============================================================\n",
        "# TEAM HEADER & CUSTOM BENCHMARK DATASET\n",
        "# ============================================================\n",
        "\n",
        "project_title = \"Sports Team Rating System\"\n",
        "dataset_name = \"Custom College Football Benchmark\"\n",
        "\n",
        "teams = [\"Team A\", \"Team B\", \"Team C\", \"Team D\", \"Team E\"]\n",
        "\n",
        "# Point-differential match results\n",
        "# A beat B by 5, B beat C by 3, etc.\n",
        "matches = [\n",
        "    (\"Team A\", \"Team B\", 5),\n",
        "    (\"Team B\", \"Team C\", 3),\n",
        "    (\"Team C\", \"Team D\", 4),\n",
        "    (\"Team D\", \"Team E\", 2),\n",
        "    (\"Team E\", \"Team A\", 1),\n",
        "    (\"Team A\", \"Team C\", 6),\n",
        "    (\"Team B\", \"Team D\", 3),\n",
        "    (\"Team C\", \"Team E\", 5),\n",
        "    (\"Team D\", \"Team A\", 2),\n",
        "    (\"Team E\", \"Team B\", 4)\n",
        "]\n",
        "\n",
        "print(\"=\" * 55)\n",
        "print(project_title)\n",
        "print(\"=\" * 55)\n",
        "print(\"Benchmark Dataset :\", dataset_name)\n",
        "print(\"Number of Teams   :\", len(teams))\n",
        "print(\"Number of Matches :\", len(matches))\n",
        "print(\"=\" * 55)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# ============================================================\n",
        "# SPORTS TEAM RATING SYSTEM (B8)\n",
        "# Using Eigenvector Centrality and Dominant Eigenvalue\n",
        "# ============================================================\n",
        "\n",
        "print(\"🏆 SPORTS TEAM RATING SYSTEM\")\n",
        "print(\"=\" * 55)\n",
        "\n",
        "print(\"\"\"\n",
        "Objective:\n",
        "5 teams play matches against each other.\n",
        "The result of each match is represented using point differentials.\n",
        "\n",
        "We construct a matrix from the match results and use:\n",
        "    1. Eigenvector Centrality\n",
        "    2. Dominant Eigenvalue\n",
        "\n",
        "to calculate and rank the teams.\n",
        "\"\"\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "oVtF3tQfDOsu",
        "outputId": "21b4dcfd-a28b-4465-a6cc-8092978bdbf8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "🏆 SPORTS TEAM RATING SYSTEM\n",
            "=======================================================\n",
            "\n",
            "Objective:\n",
            "5 teams play matches against each other.\n",
            "The result of each match is represented using point differentials.\n",
            "\n",
            "We construct a matrix from the match results and use:\n",
            "    1. Eigenvector Centrality\n",
            "    2. Dominant Eigenvalue\n",
            "\n",
            "to calculate and rank the teams.\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# ============================================================\n",
        "# IMPORTS\n",
        "# ============================================================\n",
        "\n",
        "import numpy as np\n",
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        "# SymPy is useful for displaying/checking eigenvalues\n",
        "import sympy as sp\n",
        "\n",
        "print(\"Libraries imported successfully ✅\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QHyucwy8DqUo",
        "outputId": "a4efcdcc-440f-44e4-fce0-5fb9e8413107"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Libraries imported successfully ✅\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# ============================================================\n",
        "# SPORTS TEAM RATING SYSTEM (B8)\n",
        "# Mathematics Mini Project — ABHIYAN\n",
        "# ============================================================\n",
        "\n",
        "PROJECT_TITLE = \"Sports Team Rating System (B8)\"\n",
        "PROJECT_NAME = \"Mathematics Mini Project — ABHIYAN\"\n",
        "\n",
        "print(\"=\" * 70)\n",
        "print(f\"🏆 {PROJECT_TITLE}\")\n",
        "print(f\"📘 {PROJECT_NAME}\")\n",
        "print(\"=\" * 70)\n",
        "\n",
        "print(\"\"\"\n",
        "Core Mathematics:\n",
        "• Eigenvector Centrality\n",
        "• Dominant Eigenvalue\n",
        "\n",
        "Applications:\n",
        "• Chess Ratings\n",
        "• FIFA Rankings\n",
        "• College Football Rankings\n",
        "\"\"\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lBcPbfBtEItI",
        "outputId": "49c1d991-3115-4c02-8d82-2fc9ab4a6a40"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "======================================================================\n",
            "🏆 Sports Team Rating System (B8)\n",
            "📘 Mathematics Mini Project — ABHIYAN\n",
            "======================================================================\n",
            "\n",
            "Core Mathematics:\n",
            "• Eigenvector Centrality\n",
            "• Dominant Eigenvalue\n",
            "\n",
            "Applications:\n",
            "• Chess Ratings\n",
            "• FIFA Rankings\n",
            "• College Football Rankings\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# ============================================================\n",
        "# CELL: PROJECT HEADER + INPUT CONFIGURATION\n",
        "# ============================================================\n",
        "\n",
        "PROJECT_TITLE = \"Sports Team Rating System (B8)\"\n",
        "PROJECT_VERSION = \"Customized Version 1.0\"\n",
        "\n",
        "print(\"=\" * 65)\n",
        "print(f\"🏆 {PROJECT_TITLE}\")\n",
        "print(f\"📌 {PROJECT_VERSION}\")\n",
        "print(\"=\" * 65)\n",
        "\n",
        "print(\"\"\"\n",
        "Mathematical Model:\n",
        "Eigenvector Centrality + Dominant Eigenvalue\n",
        "\n",
        "Real-World Benchmark Context:\n",
        "Chess Ratings | FIFA Rankings | College Football Rankings\n",
        "\"\"\")\n",
        "\n",
        "# ------------------------------------------------------------\n",
        "# TEAM CONFIGURATION\n",
        "# ------------------------------------------------------------\n",
        "\n",
        "teams = [\"Team A\", \"Team B\", \"Team C\", \"Team D\", \"Team E\"]\n",
        "\n",
        "# Optional team labels/descriptions\n",
        "team_info = {\n",
        "    \"Team A\": \"Strong attacking team\",\n",
        "    \"Team B\": \"Balanced team\",\n",
        "    \"Team C\": \"Defensive team\",\n",
        "    \"Team D\": \"Improving team\",\n",
        "    \"Team E\": \"Competitive team\"\n",
        "}\n",
        "\n",
        "# ------------------------------------------------------------\n",
        "# MATCH DATA\n",
        "# Format:\n",
        "# (Winner, Loser, Point Differential)\n",
        "# ------------------------------------------------------------\n",
        "\n",
        "matches = [\n",
        "    (\"Team A\", \"Team B\", 5),\n",
        "    (\"Team A\", \"Team C\", 3),\n",
        "    (\"Team D\", \"Team A\", 2),\n",
        "    (\"Team B\", \"Team C\", 4),\n",
        "    (\"Team B\", \"Team D\", 1),\n",
        "    (\"Team E\", \"Team A\", 2),\n",
        "    (\"Team C\", \"Team D\", 3),\n",
        "    (\"Team D\", \"Team E\", 4),\n",
        "    (\"Team E\", \"Team B\", 3),\n",
        "    (\"Team C\", \"Team E\", 1)\n",
        "]\n",
        "\n",
        "# ------------------------------------------------------------\n",
        "# DISPLAY CONFIGURATION\n",
        "# ------------------------------------------------------------\n",
        "\n",
        "print(\"\\n👥 TEAM CONFIGURATION\")\n",
        "print(\"-\" * 65)\n",
        "\n",
        "for team in teams:\n",
        "    print(f\"🏅 {team}: {team_info[team]}\")\n",
        "\n",
        "print(\"\\n⚽ MATCH RESULTS\")\n",
        "print(\"-\" * 65)\n",
        "\n",
        "for winner, loser, margin in matches:\n",
        "    print(f\"{winner} defeated {loser} by {margin} points\")\n",
        "\n",
        "print(\"\\n✅ Input configuration loaded successfully!\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "y9MmDuzUHwYR",
        "outputId": "292212a9-4ea5-4d38-8fca-a02cd56e3314"
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "=================================================================\n",
            "🏆 Sports Team Rating System (B8)\n",
            "📌 Customized Version 1.0\n",
            "=================================================================\n",
            "\n",
            "Mathematical Model:\n",
            "Eigenvector Centrality + Dominant Eigenvalue\n",
            "\n",
            "Real-World Benchmark Context:\n",
            "Chess Ratings | FIFA Rankings | College Football Rankings\n",
            "\n",
            "\n",
            "👥 TEAM CONFIGURATION\n",
            "-----------------------------------------------------------------\n",
            "🏅 Team A: Strong attacking team\n",
            "🏅 Team B: Balanced team\n",
            "🏅 Team C: Defensive team\n",
            "🏅 Team D: Improving team\n",
            "🏅 Team E: Competitive team\n",
            "\n",
            "⚽ MATCH RESULTS\n",
            "-----------------------------------------------------------------\n",
            "Team A defeated Team B by 5 points\n",
            "Team A defeated Team C by 3 points\n",
            "Team D defeated Team A by 2 points\n",
            "Team B defeated Team C by 4 points\n",
            "Team B defeated Team D by 1 points\n",
            "Team E defeated Team A by 2 points\n",
            "Team C defeated Team D by 3 points\n",
            "Team D defeated Team E by 4 points\n",
            "Team E defeated Team B by 3 points\n",
            "Team C defeated Team E by 1 points\n",
            "\n",
            "✅ Input configuration loaded successfully!\n"
          ]
        }
      ]
    }
  ]
}