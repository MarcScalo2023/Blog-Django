{% extends 'blog/base.html' %}
{% block title %} {{ post.title }} · Blog{% endblock %}
{% block content %}
<div>
    <h3>{{ post.title }}</h3>
    <span class="date">{{ post.created|date:"SHORT_DATE_FORMAT" }}</span>
    <p>{{ post.content }}</p>
    {% if user.is_authenticated %}
        {% for group in user.groups.all %}
            {% if group.name == 'Editores' %}
                <p>
                    <a href="{% url 'admin:blog_post_change' post.id %}" class="edit">
                        Editar entrada
                    </a>
                </p>
            {% endif %}
        {% endfor %}
    {% endif %}
    <a href="{% url 'home' %}">Volver a la portada</a>
</div>
{% endblock %}
