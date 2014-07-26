<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" type="text/css" href="resources/hex.css"></link>
    <script src="http://code.jquery.com/jquery-latest.js"></script>
</head>
<body bgcolor="{{tile['color']}}">

<h1>{{user['user']}}</h1>
<h2>{{tile['type']}}</h2>
<p>Currently Located at {{user['latitude']}}, {{user['longitude']}}</p>
<table>
    <tr>
        <td></td>
        <td>
            <form action="/north" method="post">
                <input type='hidden' name='user_id' value="{{user['_id']}}"/>
                <button type="submit">&#8593;</button>
            </form></td>
        <td></td>
    </tr>
    <tr>
        <td>
            <form action="/west" method="post">
                <input type='hidden' name='user_id' value="{{user['_id']}}"/>
                <button type="submit">&#8592;</button>
            </form>
        </td>
        <td></td>
        <td>
            <form action="/east" method="post">
                <input type='hidden' name='user_id' value="{{user['_id']}}"/>
                <button type="submit">&#8594;</button>
            </form>
        </td>
    </tr>
    <tr>
        <td></td>
        <td>
            <form action="/south" method="post">
                <input type='hidden' name='user_id' value="{{user['_id']}}"/>
                <button type="submit">&#8595;</button>
            </form>
        </td>
        <td></td>
    </tr>
</table>
<div id="commands">
    % for command in tile['commands']:
        <button type="button">{{command}}</button>
    % end
</div>


<div id="map" style="float: left; width: 400px;height:400px">
    <div style="float: left; width: 400px;height:400px">
    <div class="hex-row">
        <div class="empty"></div>
        <div data-role="page" data-direction="north" class="direction hex even" ><div class="left"></div><div class="middle"></div><div class="right"></div></div>
        <div class="empty"></div>
    </div>
    <div class="hex-row">
        <div data-direction="northwest" class="direction hex"><div class="left"></div><div class="middle"></div><div class="right"></div></div>
        <div class="hex even"><div class="direction left"></div><div class="middle"></div><div class="right"></div></div>
        <div data-direction="northeast" class="direction hex"><div class="left"></div><div class="middle"></div><div class="right"></div></div>
    </div>
    <div class="hex-row">
        <div data-direction="southwest" class="direction hex"><div class="left"></div><div class="middle"></div><div class="right"></div></div>
        <div data-direction="south" class="direction hex even"><div class="left"></div><div class="middle"></div><div class="right"></div></div>
        <div data-direction="southeast" class="direction hex"><div class="left"></div><div class="middle"></div><div class="right"></div></div>
    </div>
</div>
</div>

<script>
    $( document ).ready(function() {
        $('div.direction').click(function() {
            alert($(this).data("direction"));
        });
    });
</script>

</body>
</html>