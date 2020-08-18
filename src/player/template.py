TEMPLATE = """
<html>
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">

<body>

    <div class="container-fluid height=680px">
        <div class="row">
            <h1>{{channels[channel_id]['name']}}</h1>
        </div>
        <div class="row">
        <h2>
        {% if current_show is not none %}
            {{current_show['title']}} {{render_show_time(current_show)}}
        {% else %}
            Прямой эфир
        {% endif %}
        </h2
        </div>
        <div class="row">
            <div class="col-md-8">
                <iframe style="width:900px; height:680px;" allowfullscreen src="http://localhost:8080/channel/{{channel_id}}/embed.html?{{streaming_qs}}"></iframe>
            </div>
            {% for id, c in channels.items() %}
            <div class="col-md-2  height=680px">

                    <div>
                    <h5 class="mb-0">
                        {{c['name']}}
                    </h5>
                    <div class="list-group-item">
                        <a href="?c={{c['id']}}"> Прямой эфир</a>
                    </div>
                    {% for p in c['programme'] %}
                    <div class="list-group-item">
                        <a href="?c={{c['id']}}&p={{loop.index-1}}"> {{ p['title'] }}</a>
                        <br/>
                        {{ render_show_time (p) }}
                    </div>
                    {% endfor%}
                    </div>
            </div>
            {% endfor %}
        </div>
    </div>
    </div>
</body>

</html>
"""
