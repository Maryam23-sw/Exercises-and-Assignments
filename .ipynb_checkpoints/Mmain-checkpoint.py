{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e63435ad-335a-4d09-ba59-f4229e0451a7",
   "metadata": {},
   "outputs": [],
   "source": [
    "import Calc\n",
    "\n",
    "while True:\n",
    "    command = input(\"Enter a command ('add', 'sub', 'mult', 'div', or 'stop'): \")\n",
    "    \n",
    "    if command == \"stop\":\n",
    "        print(\"Exiting the calculator\")\n",
    "        break\n",
    "\n",
    "    if command not in [\"add\", \"sub\", \"mult\", \"div\"]:\n",
    "        print(\"This command is not found.\")\n",
    "        continue\n",
    "\n",
    "    try:\n",
    "        num1 = int(input(\"Enter the first number: \"))\n",
    "        num2 = int(input(\"Enter the second number: \"))\n",
    "    except ValueError:\n",
    "        print(\"Wrong input.\")\n",
    "        continue\n",
    "\n",
    "    if command == \"add\":\n",
    "        result = Calc.add(num1, num2)\n",
    "    elif command == \"sub\":\n",
    "        result = Calc.sub(num1, num2)\n",
    "    elif command == \"mult\":\n",
    "        result = Calc.mult(num1, num2)\n",
    "    elif command == \"div\":\n",
    "        result = Calc.div(num1, num2)\n",
    "\n",
    "    print(f\"The result of {command} is: {result}\")\n",
    "\n",
    "    cont = input(\"Need to continue or shut down? \\n press (yes or stop): \")\n",
    "    if cont == \"stop\":\n",
    "        print(\"Exiting the calculator. Goodbye!\")\n",
    "        break\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5cd9a6a1-5e08-4a10-8ee3-a1356ec1bbac",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
