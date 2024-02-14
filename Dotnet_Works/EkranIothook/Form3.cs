using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using static System.Windows.Forms.VisualStyles.VisualStyleElement;

namespace EkranIothook
{
    public partial class Form3 : Form
    {
        public Form3()
        {
            InitializeComponent();
        }

        
        private void chart1_Click(object sender, EventArgs e)
        {
            
        }
       

        private void button1_Click(object sender, EventArgs e)
        {

            chart2.Series["Yanma Sayısı"].Points.AddXY("Kırmızı", 1);
            chart2.Series["Yanma Sayısı"].Points.AddXY("Yeşil", 5);
            chart2.Series["Yanma Sayısı"].Points.AddXY("Sarı", 4);

        }

        private async void Form3_Load_1(object sender, EventArgs e)
        {

            HttpClient httpClient = new HttpClient();
            HttpRequestMessage request = new HttpRequestMessage();
            request.RequestUri = new Uri("https://iothook.com/api/device/?api_key=1c1094835fe305ad04096223&results=2");
            request.Method = HttpMethod.Get;
            request.Headers.Add("api_key", "1c1094835fe305ad04096223");
            HttpResponseMessage response = await httpClient.SendAsync(request);
            var responseString = await response.Content.ReadAsStringAsync();
            var statusCode = response.StatusCode;

            int intValue = int.Parse(responseString);

            chartGraph.Series["Yanma Sayısı"].Points.AddXY("Kırmızı", intValue);
            chartGraph.Series["Yanma Sayısı"].Points.AddXY("Yeşil", intValue);
            chartGraph.Series["Yanma Sayısı"].Points.AddXY("Sarı", intValue);

        }
    }

}
