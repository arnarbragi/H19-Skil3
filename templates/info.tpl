{% extends "base.html" %}

{% block innihald %}
    <h1>Þetta er info síðan</h1>
        <h3> {{frett[1]}} </h3>
        <h5> {{frett[2]}} </h5>
        <h5> {{frett[3]}} </h5>
        <img src="/static/{{mynd}}.jpg" height="210" width=auto>
{% endblock %}