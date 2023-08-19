<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>States</H1>
        <UL>
        {% for state in states.values() | sort(attribute='name') %}
            <LI>{{ state.id }}: <B>{{ state.name }}</B>
                <UL>
                {% for city in state.cities | sort(attribute='name')%}
                    <LI>{{ city.id }}: <B>{{ city.name }}</B></LI>
                {% endfor %}
                </UL>
            </LI>
        {% endfor %}
        </UL>
    </BODY>
</HTML>