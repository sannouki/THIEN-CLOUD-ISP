import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="http_trigger1")
def http_trigger1(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')





    resume_content = """
    Thien Ong's Resume

    Welcome to my cloud resume!

    Contact Information:
    - Email: t.ong25@ncf.edu
    - GitHub: <a href="https://github.com/sannouki">https://github.com/sannouki</a>

    Education:
    - Bachelor of Arts in Computer Science (Expected May 2026)
      New College of Florida – Sarasota, FL
    - Associate in Liberal Arts, Computer Science Path (GPA: 3.88/4.0)
      Polk State College – Lakeland, FL (May 2023)

    Extracurriculars and Awards:
    - Alumnus member of Phi Theta Kappa Honor Society
    - Nominated and awarded for All-Florida Academic Team
    - Phi Theta Kappa recognition All-USA
    - TurnPike STEM Scholar
    - Certified in Completion of Programming in C#

    Technical Skills:
    - Bilingual and native-fluent in Vietnamese
    - Proficient in Java, Python, C#
    - Human-Centered Computing for optimal user experiences
    - Development Tools: IntelliJ IDEA, Visual Studio Code, Figma, UML diagrams
    - Software Development: Object-Oriented Programming/Design (OOP/OOD), Data Structures
    - Experienced with communication tools: Skype, Discord, Teams, Zoom
    - Microsoft 365: Word, Teams, Excel, Outlook, OneDrive
    - File compression, recovery, and data organization

    Experience:
    - Jane Bancroft Cook Library – Sarasota, FL (Jan. 2024 – Current)
      - Front desk customer service addressing patron inquiries and requests
      - Maintained makerspace with 3D printers, Cricut, shirt-presses
      - Provided patron assistance in creating arts and crafts
      - Troubleshot hardware including Cricut, Macs, and 3D printers
      - Assembled Arduino robotic and embedded systems, including Raspberry Pi and Metro Uno

    - Town Tech – Auburndale, FL (June – August 2023)
      - Diagnosed software issues and performed system recovery
      - Updated operating systems, BIOS, and drivers
      - Assembled and troubleshot hardware components
      - Maintained system security by eliminating vulnerabilities

    - Rose Nails and Spa – Lakeland, FL (Jan. 2020 – Dec. 2022)
      - Resolved customer issues to ensure satisfaction
      - Improved client retention through flexibility and best practices
      - Managed financial reconciliation processes

    - Goodwill Industries International – Glendale Heights, IL (Sep. 2018 – Dec. 2019)
      - Balanced organizational tasks and customer interactions in a fast-paced environment
      - Supported operational efficiency through multitasking and teamwork
      - Operated heavy machinery including compressors and balers
    """

    return func.HttpResponse(resume_content, status_code=200)