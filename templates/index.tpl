{% extends "base.html" %}

{% block innihald %}
    <h1>Þetta er index síðan</h1>
    <h3>Fréttir dagsins</h3>
    <ul>
        {% for frett in frettir %}
            <li><a href="/frett/{{frett[0]}}">{{ frett[1] }} </a></li>
        {% endfor %}
    </ul>
    <img src="{{ url_for('static',filename='trump.jpg') }}" alt="Trump" height="210" width=auto>
{% endblock %}