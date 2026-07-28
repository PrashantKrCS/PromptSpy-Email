from dataclasses import dataclass


@dataclass
class Persona:

    name: str

    title: str

    company: str

    email: str

    def display(self):

        return f"""
Name    : {self.name}
Title   : {self.title}
Company : {self.company}
Email   : {self.email}
"""
