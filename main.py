from jinja2 import Environment, FileSystemLoader
# from weasyprint import HTML
# import pdfkit

table_placeholder = """<div class="row" >
                <table class="u-full-width">
                    <thead class="fqred">
                        <tr>
                            <th>Name</th>
                            <th>Age</th>
                            <th>Sex</th>
                            <th>Location</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Dave Gamache</td>
                            <td>26</td>
                            <td>Male</td>
                            <td>San Francisco</td>
                        </tr>
                        <tr>
                            <td>Dwayne Johnson</td>
                            <td>42</td>
                            <td>Male</td>
                            <td>Hayward</td>
                        </tr>
                    </tbody>
                </table>
            </div>
"""
temp_vars = {
    'client':'Example Client',
    'totalTraffic': 123000000,
    'percentages': {
        'total': 25.25
    },
    'source': {'bottom': 0.00,
               'bottomRange': 'Premium',
               'top': 99.98,
               'topRange': 'Critical'
    },
    'trafficType': 'Impressions',
    'implementationTech': 'JS Tag',
    'table_placeHolder': table_placeholder,
    'input' : {
        'source': 'Network',
        'subsource': 'Publisher',
        'campaign' : 'Campaign ID',
        'domain': 'Page URL'
    },
    'startDate': '1/24/2017',
    'endDate': '3/24/2017',
}


# temp_vars =
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("template.html")
html_out = template.render(temp_vars)

# pdf = HTML(html_out).write_pdf()
# with open('report.pdf', 'w') as f:
#     f.write(pdf)
with open('index.html', 'w') as f:
    f.write(html_out)

# pdfkit.from_file('index.html', 'out.pdf')
